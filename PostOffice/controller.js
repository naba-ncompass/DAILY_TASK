const axios = require("axios");
const redis = require("redis");

const getAddress = async (req, res, next) => {
  try {
    const client = redis.createClient();

    client.on("error", (err) => { console.log(err.message)})//next(Error(err.code))});

    await client.connect();

    const pin = req.query.pin;
    const value = await client.get(pin);

    if (value) {
      await client.quit()
      res.status(200).send({
        address: JSON.parse(value),
        message: "data retrieved from cache",
      });

    } else {
      const address = await axios.get(
        `https://api.postalpincode.in/pincode/${pin}`
      );
      if (address.data[0].Status === "Error") {
        next(Error("pincode doesn't exist"));
      } else {
        client.setEx(pin, 600, JSON.stringify(address.data[0].PostOffice));
        await client.quit()
        res.json({
          address: address.data[0].PostOffice,
          message: "cache miss",
        });
      }
    }

  } catch (err) {
    next(err);
  }
};
module.exports = {
  getAddress,
};
