let zoomLevel = 1;
let zoomFactor = 0.5; //How much the image is zoomed in on/out
let zoomState = 0; // 0: no zoom, can go up to 4

const imageContainer = document.getElementById('floorplan-container');
const image = document.getElementById('zoomable-image');
const zoomMaxIn = 2.0; //Max zoom in
const zoomMaxOut = 0; //Max zoom out

function resetZoom() {
  zoomLevel = 1;
  zoomState = 0;
  image.style.transform = `scale(${zoomLevel})`;
}

function zoomIn() {
    if(zoomState < 4) {
        //Zoom In
        zoomLevel = zoomLevel + zoomFactor;
        zoomState = zoomState + 1;
    }
  image.style.transform = `scale(${zoomLevel})`;
}

function zoomOut() {
    if(zoomState > 0) {
        //Zoom Out
        zoomLevel = zoomLevel - zoomFactor;
        zoomState = zoomState - 1;
    }
  image.style.transform = `scale(${zoomLevel})`;
}