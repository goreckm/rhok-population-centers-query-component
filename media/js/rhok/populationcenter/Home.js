rhok.populationcenter.Home = function(settings) {

	var self = this;
	self.settings = settings;
	var FUSTION_TABLE = 34109; // 341268; //34109;

	self.init = function(settings) {
		var html = rhok.populationcenter.soy.pages.home( {});
		settings.container.html(html);

		self.$querySection = $(".query-section");
		self.$guessMyLocation = $(".guess-my-location", self.$querySection);
		self.$coordinatesInput = $("input[name='coordinates']",
				self.$querySection);
		self.$populationCentersMap = $("#population-centers-map");
		self.$radius = $("input[name='radius']", self.$querySection);
		self.$runQuery = $(".run-query", self.$querySection);

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
					alert("Your browser doesn't support geolocation.");
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
				var circle = new CircleOverlay(map, map.getCenter(), 1,
						"#336699", 1, 1, '#336699', 0.25);
				map.addOverlay(circle);
			}

			return false;
		});

		self.$runQuery
				.click(function() {
					var url = '/ft-query';
					var requestData = {
						query : 'SELECT City, Population, Latitude, Longitude FROM ' + FUSTION_TABLE
					};
					$.getJSON(url, requestData, function(jsonData) {
						var html = rhok.populationcenter.soy.pages
								.populationcenters_result( {
									result : jsonData
								});
						$("#population-centers-result-table").html(html);
					});
				});

	};

};
