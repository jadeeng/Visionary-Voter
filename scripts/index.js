
$("path, circle").hover(function(e) {
  $('#info-box').css('display','block');
  $('#info-box').html($(this).data('info'));

});

$("path, circle").mouseleave(function(e) {
  $('#info-box').css('display','none');
});

$(document).mousemove(function(e) {
  $('#info-box').css('top',e.pageY-$('#info-box').height()-30);
  $('#info-box').css('left',e.pageX-($('#info-box').width())/2);

}).mouseover();

function fetchNames(prefix) {
  fetch(`http://localhost:8080/CandidateList?q=${prefix}`)
    .then((resp) => resp.json())
    .then(addNames);
}

function addNames(data) {
  const candidates = data.candidates;
  const ul = document.getElementById('Candidates');
  const polling_places = data.polling;
  const ul = document.getElementById('Polling');
  const events = data.events;
  const ul = document.getElementById('events');
  while (ul.firstChild) {
      ul.removeChild(ul.firstChild);
  }
  for (let candidate of candidates) {
    let li = document.createElement('li');
    let link = document.createElement('a');
    link.href = candidate.link;
    link.textContent = candidate.name;
    li.textContent = (candidate.party, candidate.district,
                      candidate.state, candidate.policies_supported,
                      candidate.level_government);
    li.appendChild(link);
    ul.appendChild(li);
  }
}

function setListener() {
  const inputEl = document.getElementById('dropdown-input');
  inputEl.addEventListener('input', () => {
    if (inputEl.value.length === 5){
      fetchNames(inputEl.value);
    }
  });
}

window.onload = setListener;
