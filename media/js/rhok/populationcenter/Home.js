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

		self.$guessMyLocation.click(function() {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition(function(position) {
					self.$coordinatesInput.val(position.coords.latitude + ","
							+ position.coords.longitude);
				});
			}
		});
	};

};
