"use strict";

// This code is based on the demo for the Google Maps lecture (bears.js),
// examples from the Google Maps JavaScript API docs, and an example from the
// AJAX lecture.

//////////////////////
// global variables //

var map;

//////////////////////

function init(){
    initMap();
}

function initMap(){

    var directionsDisplay = new google.maps.DirectionsRenderer();
    var directionsService = new google.maps.DirectionsService();

    // Create a map object and specify the DOM element for display.
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 37.7886794, lng: -122.41153689999999},  // Hackbright
        zoom: 12,
        mapTypeControl: false,
        streetViewControl: false,
    });

    // FIXME: Disabled for demoing.
    // Try HTML5 geolocation; if successful, center map on user location.
    // if (navigator.geolocation) {
    //     navigator.geolocation.getCurrentPosition(function (position) {
    //         var initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    //         console.log(initialLocation.lat(), initialLocation.lng());
    //         map.setCenter(initialLocation);
    //         console.log("Geolocation and recentering successful.");
    //     });
    // }

    calculateAndDisplayRoute(directionsService, directionsDisplay);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    var start = {lat: 37.7886794, lng: -122.41153689999999};
    var end = {lat: 37.7886794, lng: -122.41153689999999};
    var waypts = [];

    var responseWaypoints = art_list;

        for (var i = 0; i < responseWaypoints.length; i++) {
            waypts.push({
                location: responseWaypoints[i],
                stopover: true
            });
          }

    directionsService.route({
      origin: start,
      destination: end,
      waypoints: waypts,
      optimizeWaypoints: true,
      travelMode: 'WALKING',
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);
        directionsDisplay.setMap(map);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
}

google.maps.event.addDomListener(window, 'load', init);
