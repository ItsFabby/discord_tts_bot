import boto3
import discord
import asyncio

import constants as c

polly_client = boto3.Session(
    aws_access_key_id=c.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=c.AWS_SECRET_ACCESS_KEY,
    region_name=c.AWS_REGION_NAME
).client('polly')


async def tts_message_controller(client, message):
    if message.content.startswith(c.TTS_SAY_VOICE):
        await _tts_say_voice(client, message)
        return
    if message.content.startswith(c.TTS_SAY):
        await _tts_say(client, message)
        return
    if message.content.startswith(c.TTS_LEAVE):
        await _leave(client)
        return
    if message.content.startswith(c.TTS_VOICES):
        await _voices(message)
        return
    await _help(message)


async def _voices(message):
    allowed_voices = str(list(c.VOICES.keys())).replace('\'', '')
    await message.channel.send(f"Allowed voices: {allowed_voices}\r")


async def _help(message):
    allowed_voices = str(list(c.VOICES.keys())).replace('\'', '')
    await message.channel.send(
        f"!tts say <message>\r"
        f"!tts say-<voice> <message>\rAllowed voices: {allowed_voices}\r"
        f"!tts leave"
    )


async def get_tts(content, channel_id, client, voice='Ivy'):
    content = content[:c.CHARACTER_LIMIT]

    voice_client = await _join(client, channel_id)

    response = polly_client.synthesize_speech(
        VoiceId=voice,
        OutputFormat='mp3',
        Text=content,
        SampleRate='16000'
    )

    file = open('speech.mp3', 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    source = discord.FFmpegOpusAudio('speech.mp3')
    await asyncio.sleep(1)
    voice_client.play(
        source
    )


async def _tts_say_voice(client, message):
    lang = message.content.split('-')[1].split(' ')[0]

    if lang not in c.VOICES.keys():
        allowed_voices = str(list(c.VOICES.keys())).replace('\'', '')
        await message.channel.send(
            f'Voice not valid. Try "!tts say-<voice> <message>". \r '
            f'Valid voices : {allowed_voices}'
        )
        return

    voice = c.VOICES[lang]
    content = ' '.join(message.content.split(' ')[2:])
    channel_id = message.author.voice.channel.id
    await get_tts(content, channel_id, client, voice=voice)


async def _tts_say(client, message):
    content = message.content.split(c.TTS_SAY)[1]
    channel_id = message.author.voice.channel.id
    await get_tts(content, channel_id, client)


async def _join(client, channel_id):
    current_voice_client = await _leave(client, channel_id)
    if current_voice_client:
        return current_voice_client

    voice_channel = client.get_channel(channel_id)
    return await voice_channel.connect()


async def _leave(client, channel_id=None):
    current_voice_client = None
    for voice_client in client.voice_clients:
        if voice_client.channel.id == channel_id:
            current_voice_client = voice_client
        else:
            await voice_client.disconnect()
    return current_voice_client
