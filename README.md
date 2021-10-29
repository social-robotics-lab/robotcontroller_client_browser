# robotcontroller_client_browser
Sample programs for communicating with Sota (CommU) using Web browser.


# Install
```
git clone https://github.com/social-robotics-lab/robotcontroller_client_browser.git
cd robotcontroller_client_browser
docker build -t robotcontroller_client_browser .
```

# Run
## Sota
```
java -jar RobotController.jar
```

## Client
```
docker run --rm --name robotcontroller_client_browser --mount type=bind,source="$(pwd)"/src,target=/tmp -p 8000:8000 -it robotcontroller_client_browser /bin/bash
python3 -m http.server --cgi 8000
```

Let's check 'http://localhost:8000' In a web browser.
