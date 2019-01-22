import click
import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


@click.command()
@click.option('--host', default='test.mosquitto.org',
              help='The mqtt broker to connect to.')
@click.option('--port', default=1883,
              help='The mqtt broker port to connect to.')
@click.option('--topic', default='hackher413Workshop',
              help='The mqtt topic to send/receive on.')
@click.option('--message',
              help='If message is passed, sends message instead of listening')
def mqtt_cli(host, port, topic, message):
    """Simple MQTT CLI tool for sending and receiving MQTT Messages."""

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port, 60)

    print('Connecting to %s:%s' % (host, port))
    if message:
        click.echo('Sending to Topic: %s' % topic)
        click.echo('Message Sent: %s' % message)
        client.publish(topic, message)  # publish
    else:
        click.echo('Listening on Topic: %s' % topic)
        # Subscribing outside of on_connect() means that if we lose the
        # connection and reconnect then subscriptions won't be renewed.
        client.subscribe(topic)
        # Blocking call that processes network traffic, dispatches
        # callbacks and handles reconnecting.
        client.loop_forever()


if __name__ == '__main__':
    mqtt_cli()
