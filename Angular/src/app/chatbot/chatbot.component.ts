import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';
import { Http } from '@angular/http';

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {
  public chatbotHtml: string = ""
  constructor(http: Http) {
    // http.get("https://thenoobsway.com/webbot/webchatbot.html").map((html:any) => {
    //   console.log(html);
    //   this.chatbotComponent = html
    // });
   }

  ngOnInit() {
    $.ajax({url:"https://thenoobsway.com/webbot/webchatbot.html",
    'responseType':'application/json',
          'cache': false,
          "async": true,
          "crossDomain": true,
          "method": "GET",
          success: function(data) {
            this.chatbotHtml = data;
            console.log(this.chatbotHtml)
          }})
  }

}
