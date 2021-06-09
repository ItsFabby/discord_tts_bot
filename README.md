# Text to speech bot for Discord

## About the Project

This project allows to use text to speech in discord voice channels. After writing a message with the command `!tts say`, 
 the bot joins your voice channel to read out the message. You can choose from variety of male and female voices 
in different languages. A (free) AWS account is needed.

## Build With

- [Amazon Polly](https://aws.amazon.com/polly/)
- [discord.py](https://discordpy.readthedocs.io/)
- [FFmpeg](https://www.ffmpeg.org/)

## Getting Started

1. Create an [AWS](https://aws.amazon.com/) account (or use an existing one). It is advisable to create an IAM user with
   only access to the Polly service.


2. Enter the following credentials of the IAM role in `.env`:
    * Access key ID
    * Secret access key
    * Region

Amazon Polly allows 5 million characters per month for 12 months for free.

3. Go to [https://discord.com/developers/applications](https://discord.com/developers/applications) and create a new
   application. Under "OAuth2" choose scope "bot" and use the link to add the bot to your discord server. You might need
   to give extra permissions.


4. Under "Bot" you can find your token. Copy it to `.env`.


5. [Optional] Host the program on a server to have it running 24/7. You can use a free AWS EC2 instance for this.


6. Install [FFmpeg](https://www.ffmpeg.org/) and make sure to set up the path correctly.


7. Run `__main__.py` with a Python interpreter.

## How to Use

- Type `!tts say <message>` (replace `<message>`) in any text channel while being in a voice channel. The bot will join
  your channel and say the message.


- `!tts say-<voice> <message>` (replace `<voice>` e.g. with `ge1`) allows you to use other voices. Use `!tts voices`
  to see all available voices.


- Use `!tts leave` to kick the bot from the voice channel.

## License

Distributed under the MIT License. See `LICENSE` for more information.
