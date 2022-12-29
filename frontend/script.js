// Node display elements
const imagePath = "../static/img/";
const nodeImage = document.getElementById("node-image");
const currentNodeText = document.getElementById("current-node");
const currentHeadingText = document.getElementById("current-heading");

// Nav buttons
const buttonCounterclockwise = document.getElementById("counterclockwise");
const buttonForward = document.getElementById("forward");
const buttonClockwise = document.getElementById("clockwise");

// Start at node 1 facing north
var currentNodeID = 1;
var currentHeading = 0;

// Browser support https://caniuse.com/async-functions
async function postTravelData(reqBody) {
    try {
      const response = await fetch ("http://127.0.0.1:8000/travel", {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        mode: "cors", // no-cors, *cors, same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(reqBody) // body data type must match "Content-Type" header
      });
      console.log(response);
      const data = await response.json();
      console.log(data);
      // Shorthand, v useful https://caniuse.com/mdn-javascript_operators_destructuring
      // const { message } = data;
      updatePosition(data);
    } catch (error) {
      // Do any error handling here
      console.log(error);
    }
}

function inputRouter(movementType) {
  var requestBody = new Object();
  requestBody.current_node_id = currentNodeID;
  requestBody.current_heading = currentHeading;
  // This relies on the button & page load functions passing the exact movement
  // name to inputRouter that the API is expecting
  requestBody.direction = movementType; 
  postTravelData(requestBody);
}

function updatePosition(responseData) {
  // Update the image element
  fullNodeImagePath = imagePath + responseData.node_image; // there's probably a better way to do this
  nodeImage.src = fullNodeImagePath;
  
  // Update position & heading vars
  currentNodeID = responseData.node_id;
  currentHeading = responseData.heading;

  // Display position & heading on page
  currentNodeText.innerHTML = "Current node ID: " + currentNodeID;
  currentHeadingText.innerHTML = "Current heading: " + currentHeading;
}

// On page load, call the "here" movement
// to get the current (initial) location's node image
window.onload = function() {
  inputRouter("here");
}

// Button functions
buttonCounterclockwise.onclick = function() {
  inputRouter("counterclockwise");
}

buttonForward.onclick = function() {
  inputRouter("forward");
}

buttonClockwise.onclick = function() {
  inputRouter("clockwise");
}
