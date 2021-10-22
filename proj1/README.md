The way I approached this project was first getting the arguments correct,
I then figured out how to create and connect sockets,
Then I figured out the actual sending and receiving of the messages
I especially wanted to make sure that every message was being fully read, so I implemented
a loop that continuously reads incoming messages until encountering a \n.
Then depending on the type of message received the program would continuously do the counting
instructed by the messages until receivng a BYE message.
Finally I implemented the option for the ssl wrapper.

My biggest issues stemmed from trying to figure out how to wrap the socket in tsl/ssl encryption.

I tested my code using print statements throughout.
