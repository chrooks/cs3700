First wanted to get the argument handling done, so I used argparse for that.

Then for each url I used urlparse to parse the urls, and created Connection objects that stored
the socket and other necessary information.

The program then checks the operation argument and does the necessary funciton calls.

I implemented the login and all the rest of the commands for establishing the control channel.

I then implemmented mkd, rmd, and dele because they didn't require a data channel to be open.

I implemented pasv and used a helper to parse the information from the response.

I then implemented list following RFC 4217 protocol.

Then I implemented stor and retr.

Lastly I went through the conditional that handles the operations and implemented their functionality using the functions for the commands.

    - mv and cp were tricky because I needed to determine which url was local and which was remote
    - I fixed this by checking if the supplied url had a scheme, if not it was flagged local when creating the Connection object