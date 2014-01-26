function PopulateEvents(data) {                                                              
    console.log(data.data);                                                        
    var cal = data.data;                                                           
    for(i = 0; i < cal.length; i++) {                                              
        var ev = "";
        ev = "<section class='event'> <div class='event-cal'> <div class='event-date'> <span class='event-date-day'>"
        $("#events").append(ev);                      
        console.log(cal[i].summary);                                               
    }                                                                              
    console.log(data.data.length);                                                 
}                                                                                  
<script src="http://compsoc.api1.hasacalendar.co.uk/event/jsonp?callback=PopulateEvents"></script>
//<section class="event">
//<div class="event-cal">
//<div class="event-date">
//<span class="event-date-day">{{ event.when|date:'D' }}</span>
//<span class="event-date-num">{{ event.when|date:'dS' }}</span>
//<span class="event-date-mon">{{ event.when|date:'M Y' }}</span>
//</div>
//<div class="event-time">{{ event.when|date:'H:i' }}</div>
//</div>
//<div class="event-description">
//<h2>{{ event.title }}</h2>
//<p>{{ event.description }}</p>
//</div>
//<div style="clear: both;"></div>
//</section>
