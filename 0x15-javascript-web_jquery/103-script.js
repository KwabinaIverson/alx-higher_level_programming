$(document).ready(function() {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();

    // Ensure language code is not empty
    if (languageCode.trim() !== '') {
      // Fetch translation from API
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`, function(data) {
        $('#hello').text(data.hello);
      });
    }
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(event) {
    // Check if Enter key is pressed
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
