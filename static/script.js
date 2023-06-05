function startRecognition() {
  var recognition = new webkitSpeechRecognition();
  recognition.lang = "pt-BR";

  recognition.onresult = function (event) {
    var query = event.results[0][0].transcript;
    $("#queryInput").val(query);
    $("#searchForm").submit();
  };

  recognition.start();
}
