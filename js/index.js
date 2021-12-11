/*
    Storing the account SID and AUTH Token
    as environment variables for security purposes.
    For more info: https://twil.io/secure
*/
const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;

const Twilio = require("twilio");

const client = new Twilio(accountSid, authToken);

// Displays the most recent message sent from your Twilio account
client.messages
    .list()
    // JS Promise that returns the messages:
    .then((messages) => {
        console.log(`The most recent message is ${messages[0].body}`);
    })
    .catch((err) => console.error(err));
