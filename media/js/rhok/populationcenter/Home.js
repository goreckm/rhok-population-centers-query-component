rhok.populationcenter.Home = function(settings) {

	var self = this;
	self.settings = settings;

	self.init = function(settings) {
		var html = rhok.populationcenter.soy.pages.home( {});
		settings.container.html(html);

		self.$querySection = $(".query-section");
		self.$guessMyLocation = $(".guess-my-location", self.$querySection);
		self.$coordinatesInput = $("input[name='coordinates']",
				self.$querySection);
		self.$populationCentersMap = $("#population-centers-map");

		var myOptions = {
			zoom : 6,
			mapTypeId : google.maps.MapTypeId.ROADMAP
		};
		var map = new google.maps.Map(document
				.getElementById("population-centers-map"), myOptions);
		var browserSupportFlag = false;

		self.$guessMyLocation.click(function() {
			var coordinates = undefined;
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition(function(position) {
					coordinates = {
						latitude : position.coords.latitude,
						longitude : position.coords.longitude
					};
					centerMap(coordinates);
				}, function() {
					handleNoGeolocation(browserSupportFlag);
				});
				// Try Google Gears Geolocation
			} else if (google.gears) {
				browserSupportFlag = true;
				var geo = google.gears.factory.create('beta.geolocation');
				geo.getCurrentPosition(function(position) {
					coordinates = {
						latitude : position.latitude,
						longitude : position.longitude
					};
					centerMap(coordinates);
				}, function() {
					handleNoGeoLocation(browserSupportFlag);
				});
				// Browser doesn't support Geolocation
			} else {
				browserSupportFlag = false;
				handleNoGeolocation(browserSupportFlag);
			}

			function handleNoGeolocation(errorFlag) {
				if (errorFlag == true) {
					alert("Geolocation service failed.");
				} else {
					alert("Your browser doesn't support geolocation. We've placed you in Siberia.");
				}
			}

			function centerMap(center) {
				var location = new google.maps.LatLng(center.latitude,
						center.longitude);
				map.setCenter(location);
				var marker = new google.maps.Marker( {
					position : location,
					map : map,
					animation : google.maps.Animation.DROP,
					title : center.latitude + "," + center.longitude
				});
			}

			return false;
		});

	};

};
