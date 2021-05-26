# streamlit_docker_logging_example
An example of using streamlit with logging with docker.

![log.JPG](log.jpg)

### High Level:
Due the fact that streamlit does not allow us at this point to use "logging" and save it inside a file, i've found a workaround.

----
in this code you may see an example of how to use logging together with docker.

- when running this, an image will be created, on startup, the start_app.sh will initiat, it contains the command which will run the app with the option of saving the output of the console inside the declared file.

- In the GUI ive made a simple function that will display the logs, it will update each time the page is open, meaning every refresh of the page, a new log will be created, therefore each refresh a new line will be written.

- written using streamlit 0.82.0

More:
- [How to show logs inside the GUI in real time](https://github.com/BugzTheBunny/streamlit_logging_output_example)
