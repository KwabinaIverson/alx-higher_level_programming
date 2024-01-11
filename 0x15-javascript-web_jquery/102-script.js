$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    
    // Ensure language code is not empty
    if (languageCode.trim() !== '') {
      // Fetch translation from API
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`, function(data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
