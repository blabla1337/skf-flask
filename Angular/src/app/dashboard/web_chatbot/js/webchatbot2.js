var accessToken = "07be0e8c62b14d6e8aabccf787dc87b7";
var baseUrl = "https://api.api.ai/v1/";
var chatBotImagePath = 'images/logo-purple.png';
var chat = "";
var doc;
var crossImage = '';
var ruiImage = '';
var jq;
var templateVisited = 1;
if(typeof($) != 'undefined'){
	jq = $;
} else if(typeof(jquery) != 'undefined'){
	jq = jquery;
}
if(jq){	
	(function($){
		$(document).ready(function() {
			function getDataURL(url){
	            return new Promise(function(resolve, reject){
	                fetch(url, {credentials: 'omit'}).then(function(response){
	                    response.blob().then(function(blob){
	                        var reader = new FileReader();
	                        reader.onloadend = function(){
	                            resolve(reader.result);
	                        }
	                        reader.onerror = function(error){
	                            reject(error);
	                        }
	                        reader.readAsDataURL(blob);
	                    });
	                }); 
	            });
	        }
	        getDataURL("images/download.svg")
	            .then(function(dataUrl){
	                crossImage = dataUrl;
	        	});
	        getDataURL("images/download.svg")
	            .then(function(dataUrl){
	                ruiImage = dataUrl;
	            });
			$('.chatbox').on('click keyup', function(){
				msg = $('#textmsg').val();
				msg = trimMessage(msg);
				if(msg){
					$('#send').show();
				}
				if(!msg){
					$('#send').hide();
				}
				if((event.target.id == 'textmsg' && event.keyCode === 13) || (event.type == "click" && event.target.innerText == 'Send ')){
					$('#send').hide();
					var msg = event.target.value || $('#textmsg').val();
					sendRequestToDialogFlow('chat self', '', msg);
					$('#textmsg').val('');
				}
			});

			$('#close').on('click', function(){
				closeChat();
			});

			$('.started').on('click', function(){
				var getStarted = false;
				if(!getStarted){
					sendRequestToDialogFlow('chat self', '', "Get Started");
					getStarted = true;
				}
				$('.firstScreen').hide();
				$('.chatbox').show();
			});

			$('.chatbot-btn').on('click', function(){
				if(sessionStorage.getItem("chatHtml") != null) {
					jsForCreateHtml(sessionStorage.getItem("chatHtml"));
				}
				chat = $('#chatlogs').html();
				chat = trimMessage(chat);
				if(chat){
					$('.chatbox').stop().show();
					$('#chatlogs').animate({scrollTop: $('#chatlogs')[0].scrollHeight});
				}
				else{
					$('.firstScreen').stop().show();
				}
				if(($('.chatbot-btn img').attr('src') == "images/download.svg" && $('.chatbot-btn img').attr('class') == 'remove') || $('.chatbot-btn object').attr('data') == ruiImage){
					$('.chatbot-btn img').css("display", "none").removeClass("remove");
					$('.chatbot-btn object').show().attr('data', crossImage);
					$('.chatbot-btn').css("border-radius", "50% 50% 50% 50%");
				}
				else{	
					$('.chatbot-btn').css("border-radius", "50% 50% 50% 50%");
					$('.chatbot-btn object').attr('data', ruiImage);
					$('.chatbox, .firstScreen').stop().hide();
				}
			});
		});

		function closeChat(){
			$('.chatbot-btn').click();
		}

		function trimMessage(msg){
			msg && (msg = msg.trim());
			return msg;
		}

		function validate(msg, validationCondition){
			return new Promise(function(resolve, reject){
				if(!msg || msg == validationCondition)
					reject();
				resolve();
			})
		}

		function generalScript(){
			$('.btnss').hide();
		}

		function sendRequestToDialogFlow(chatClass, photoUrl, msg = null, title = null) {
			msg = trimMessage(msg);

			validate(msg, '').then(function(){
				generalScript();
				$.ajax({
					type: "POST",
					url: baseUrl + "query?v=20150910",
					contentType: "application/json; charset=utf-8",
					dataType: "json",
					headers: {
						"Authorization": "Bearer " + accessToken
					},
					data: JSON.stringify({ query: msg, lang: "en", sessionId: "somerandomthing" }),
					success: function(data) {
						loader();
						setTimeout(function(){
							processData(data);
						}, 1000);
					},
					statusCode: {
				    	500: function() {
							errorMessage("I am offline. Please reach out after some time. Please leave a message if you wish to and I'll make sure it reaches our team.");
					    },
					    501: function() {
							errorMessage("I am offline. Please reach out after some time. Please leave a message if you wish to and I'll make sure it reaches our team.");
					    },
					    502: function() {
							errorMessage("I am offline. Please reach out after some time. Please leave a message if you wish to and I'll make sure it reaches our team.");
					    },
					    503: function() {
							errorMessage("I am offline. Please reach out after some time. Please leave a message if you wish to and I'll make sure it reaches our team.");
					    },
					    504: function() {
							errorMessage("I am offline. Please reach out after some time. Please leave a message if you wish to and I'll make sure it reaches our team.");
					    },
					    505: function() {
							errorMessage("I am offline. Please reach out after some time. Please leave a message if you wish to and I'll make sure it reaches our team.");
					    }
					},
					error: function(data) {
						errorMessage("Please check your internet connection.");
					}
				});
				var message = msg;
				if(title){
					message = title;
				}
				createHtml(chatClass, photoUrl, message);
			})
			.catch(function(res){
				//console.log('Empty message');
			})
		}

		function processData(msg){
			var chatClass = 'chat friend';
			var action;
			var result = msg.result;
			if(result){
				if(result.action){
					action = result.action;
					action = action.match(/smalltalk/gi);
				}
			}
			var messages = msg.result.fulfillment.messages;
			for(var i = 0; i < messages.length; i++){
				if(messages[i].replies){
					var text = messages[i].title;
					createHtml(chatClass, chatBotImagePath, text,'', messages[i].replies, "replies");
				}
				if(messages[i].platform == "facebook"){
					if(messages[i].speech){
						text = messages[i].speech;
						createHtml(chatClass, chatBotImagePath, text);
					}
					if(messages[i].payload){
						if(messages[i].payload.facebook.attachment){
							if(messages[i].payload.facebook.attachment.text){
								text = messages[i].payload.facebook.attachment.text;
								createHtml(chatClass, chatBotImagePath, text);
							}
							var cards_payload = messages[i].payload.facebook.attachment.payload;
							if(cards_payload && cards_payload.template_type == "generic"){
								if(cards_payload.elements){
									templateVisited = 0;
									cards_element = cards_payload.elements;
									createHtml(chatClass, chatBotImagePath, '', '', cards_element, "templateCards");
								}
							}
						}
					}
				}
				if(messages[i].payload){
					if(messages[i].payload.facebook.attachment && templateVisited){
						var visit_payload = messages[i].payload.facebook.attachment.payload;
						if(visit_payload){
							if(visit_payload.elements){
								visit_element = visit_payload.elements;
								createHtml(chatClass, chatBotImagePath, '', '', visit_element, "visitCards");
							}
						}
					}
				}
				if(messages[i].payload){
					var payload = messages[i].payload;
					if(payload.facebook && payload.facebook.quick_replies || payload.facebook.attachment.quick_replies){
			   			createHtml(chatClass, chatBotImagePath, payload.facebook.text, '', payload.facebook.quick_replies || payload.facebook.attachment.quick_replies, "qr");
			   		}
				}
				if(messages[i].platform == "facebook" && messages[i].payload){
					if(messages[i].payload.facebook.attachment){
						var template_payload = messages[i].payload.facebook.attachment.payload;
						if(template_payload.template_type == "button" && typeof template_payload.buttons !== "undefined"){ 
							createHtml(chatClass, chatBotImagePath, '', '', template_payload, "templateButton");
						}
					}
				}
				if(action){
					if(action[0] == "smalltalk"){
						if(messages[i].speech){
							createHtml(chatClass, chatBotImagePath, messages[i].speech);
						}
					}
				}
			}
		}

		function errorMessage(msg){
			var chatClass = 'chat friend';
			createHtml(chatClass, chatBotImagePath, msg);
		}

		function createHtml(chatClass, photoUrl, msg, title = null, response = null, type = null){
			var html = "";
			var styles = "";
			if(chatClass == "chat friend"){
				styles = "display: none;";
			}
			if(msg){
				html = '<div class = "'+ chatClass +'" style = "'+ styles +'">\
					<p class="chat-message">'+ msg +'</p>\
					<div class = "user-photo">\
						<img src = "'+ photoUrl +'">\
					</div>\
				</div>';
			}
			html = replies(response, html, type);
			html = templateButton(response, html, type);
			html = templateCards(response, html, type);
			html = visitCards(response, html, type);
			html = quickReply(response, html, type);

			jsForCreateHtml(html, response);	
		}

		function quickReply(response, html, type){
			if(response && type == "qr"){
				html += '<div class = "btnss">';
				for(var j = 0; j < response.length; j++){
					html += '<input type="button" class ="btns" payload="'+ response[j].payload +'" index="' + j + '" value="' + response[j].title + '"/>';
				}
				html += '</div>';
			}
			return html;
		}
		var attached = false;
		function jsForCreateHtml(html, response){
			var element = $('.chatlogs');
			hideLoader();
			$(html).appendTo(element);
			$('.chat.friend').show();
			$('.friend .chat-message').show("slow");
			$('.btnss').css("opacity", 1);
			if($('.btns').length){
				$('.btns').on('click', function(){
					var id = $(this).attr('index');
					var payload = $(this).attr("payload");
					var title = $(this).val();
					sendRequestToDialogFlow('chat self', '', payload, title);
				});
			}
			if($('.replies').length){
				$('.reply').on('click', function(){
					var id = $(this).attr('index');
					sendRequestToDialogFlow('chat self', '', response[id]);
				});
			}

			if($('.templateButtons').length && !attached){
				attached = true;
				$('.templateButtons').on('click', function(e){
					var id = $(this).attr('index');
					var payload = $(this).attr("payload");
					var title = $(this).val();
					sendRequestToDialogFlow('chat self', '', payload, title);
				});
			}
			if($('.cardsButtons').length){
				$('.cardsButtons').on('click', function(){
					var id = $(this).attr('index');
					try{
						for(i = 0; i < response.length; i++){
							sendRequestToDialogFlow('chat self', '', response[i].buttons[id].payload, response[i].buttons[id].title);
							break;
						}
					}
					catch(err){
						//console.log("cards button error", err);
					}
				});
			}
			$('.visitUrl').on('click', function(e) {
				var wholeChat = $('.chatlogs').html();
				sessionStorage.setItem("chatHtml", wholeChat);
			});
			$('#chatlogs').animate({scrollTop: $('#chatlogs')[0].scrollHeight});

		}

		function replies(response, html, type){
			if(response && type == "replies"){
				html += '<div class = "btnss replies" >';
				for(var j = 0; j < response.length; j++){
					html += '<input type="button" class ="reply"  index="' + j + '" value="' + response[j] + '"/>';
				}
				html += '</div>';
			}
			return html;
		}

		function templateButton(response, html, type){
			if(response && type == "templateButton"){
				html += '<div class = "chat friend">\
				<div class = "user-photo">\
					<img src = "'+ chatBotImagePath +'">\
				</div>\
				<div class = "templateButton">\
					<div class="templateText">\
						<p class="text">'+response.text+'</p>\
					</div>';
				for(var j = 0; j < response.buttons.length; j++){
					if(response.buttons[j].payload){
						html += '<input type="button" class ="templateButtons"  payload="'+ response.buttons[j].payload +'"index="' + j + '" value="' + response.buttons[j].title + '"/>';
					}
					if(response.buttons[j].url){
						html += '<a href = "'+response.buttons[j].url+'" target = "_blank" class = "templateButtons">'+response.buttons[j].title+'</a>';
					}
				}
				html += '</div>\
				</div>';
			}
			return html;
		}

		function templateCards(response, html, type){
			if(response && type == "templateCards"){
				html += '<div class = "chat friend">\
				<div class = "user-photo">\
					<img src = "'+ chatBotImagePath +'">\
				</div>\
				<div class = "allTemplateCards">';
				for(i = 0; i < response.length; i++){
					html += '<div class = "templateCards">\
						<div class="templateImage">\
							<img src="'+ response[i].image_url+'">\
						</div>\
						<div class="cardsText">\
							<div class="cardsTitle">\
								<p>'+ response[i].title +'</p>\
							</div>';
					if(response[i].subtitle){
						html += '<div class="cardsSubtitle">'+ response[i].subtitle +'</div>';
					}
					html += '</div>\
					<div class="allCardsButtons">';
					for(var j = 0; j < response[i].buttons.length; j++){
						if(response[i].buttons[j].url){
							html += '<a href = "'+response[i].buttons[j].url+'" target = "_blank" class = "cardsButtons">'+response[i].buttons[j].title+'</a>';
						}
						if(response[i].buttons[j].payload){
							html += '<input type="button" class ="cardsButtons"  index="' + j + '" value="' + response[i].buttons[j].title + '"/>';
						}
					}
					html += '</div>\
					</div>';
				}
				html += '</div>\
				</div>';
			}
			return html;
		}

		function visitCards(response, html, type) {
			if(response && type == "visitCards"){
				html += '<div class="visitCardss">';
				for(i = 0; i < response.length; i++) {
					html += '<p>'+response[i].title+'</p>';
					for(j = 0; j < response[i].buttons.length; j++) {
						html += '<a href="'+response[i].buttons[j].url+'" class="visitUrl">'+response[i].buttons[j].title+'</a>';
					}
				} 
			}
			return html;
		}

		function loader() {
			html = '<div class = "loader" style = "display: hidden;">\
						<img src = "images/loader3.gif">\
						<div>\
					</div>';
			$(html).appendTo($('.chatlogs'));
			$(this).show();
			$('#chatlogs').animate({scrollTop: $('#chatlogs')[0].scrollHeight});	
		}

		function hideLoader(){
			$('.loader').hide();
		}
	}(jq));
} else {
	var s = document.createElement("script");
	s.type = "text/javascript";
	s.src = "js/jquery.min.js";
	$("head").append(s);
}
