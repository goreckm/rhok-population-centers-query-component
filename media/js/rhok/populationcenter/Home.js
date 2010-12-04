rhok.populationcenter.Home = function(settings) {
	
	var self = this;
	self.settings = settings;

	
	self.init = function(settings) {
		var html = rhok.populationcenter.soy.pages.home({});
		settings.container.html(html);
	};
	
};
