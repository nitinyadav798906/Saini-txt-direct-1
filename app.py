from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="https://tinypic.host/images/2025/04/14/1000000208.th.jpg">
    <titleSudoR2spr Repository</title>
	<link rel="icon" type="image/x-icon" href="https://tinypic.host/images/2025/04/14/1000000208.th.jpg">

</head>

<body>
    <div class="container" style="bg-dark text-red text-center py-3 mt-5">
        <a href="https://github.com/nitinyadav798906" class="card">
            <p>
              

                <b>v2.0.0</b>
            </p>
        </a>
    </div>
	<br></br><br></br><br></br>
	<footer class="bg-dark text-white text-center py-3 mt-5">
	<center><img loading="lazy" class="object-none object-center" src="https://tinypic.host/images/2025/04/14/1000000208.th.jpg" width="240" height="120">
        Powered By sky 
		<img loading="lazy" class="object-none object-center" src="https://tinypic.host/images/2025/04/14/1000000208.th.jpg" width="240" height="120">
		<div class="footer__copyright">
            <p class="footer__copyright-info">
                © 2024 Video Downloader. All rights reserved.
            </p>
        </div>
    </footer></center>
</body>

</html>
"""


if __name__ == "__main__":
    app.run()
