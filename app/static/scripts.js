// add text to the Output area
function addOutputText(text) {
  let output = document.getElementById('outputText');
  output.innerText = text;
}

// send an HTTP POST request to the server on submissions
$(document).ready(function() {
  $('form').on('submit', function(event) {

    $.ajax({
      data : {
        content : $('#textArea').val()
      },
      type : 'POST',
      url : '/process'
    })
    .done(function(data) {
      // display Error alert for bad inputs
      if (data.error) {
        $('#errorAlert').text(data.error).show()
        addOutputText('');
      }
      // display model output on success
      else {
        addOutputText(data.result);
        $('#errorAlert').hide()
      }
    })
    // prevent a page refresh on submissions
    event.preventDefault()
  })
})

// display character count within the text area
function countChars(obj){
  var maxLength = 500;
  var strLength = obj.value.length;
  var charRemain = maxLength - strLength;

  if(charRemain < 0){
    document.getElementById('charNum').innerHTML = '<p style="color:red;">You have \
     exceeded \the limit of '+ maxLength + ' characters</p>';
  }
  else{
    document.getElementById('charNum').innerHTML = charRemain + ' characters remaining';

  }
}
