const Twilio = require("twilio");

const client = new Twilio("AC3beedfaa2c10cf264c5f55a9fbd8f947", "317ae7a4e83cd96b5603cfc0ff30b1e9");

client.messages
    .list()
    .then((messages) => {
        console.log(`The most recent message is ${messages[0].body}`);
    })
    .catch((err) => console.error(err));
