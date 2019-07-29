
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
  const candidate_ul = document.getElementById('Candidates');
  while (candidate_ul.firstChild) {
      ul.removeChild(ul.firstChild);
  }
  // const polling_places = data.polling;
  // const polling_places_ul = document.getElementById('Polling_places');
  // while (ul.firstChild) {
  //     ul.removeChild(ul.firstChild);
  // const polling_places = data.polling;
  // const events_ul = document.getElementById('Events');
  // while (ul.firstChild) {
  //         ul.removeChild(ul.firstChild);
  for (let candidate of candidates) {
    let li = document.createElement('li');
    let link = document.createElement('a');
    link.href = candidate.link;
    link.textContent = " " + candidate.name;
    li.textContent = (candidate.party, candidate.district,
                      candidate.state, candidate.policies_supported,
                      candidate.level_government);
    li.appendChild(link);
    candidate_ul.appendChild(li);
  }
  for (let events of eventss) {
    let li = document.createElement('li');
    li.textContent = (events.description, events.candidates);
    li.appendChild(link);
    ul.appendChild(li);
  }
  for (let polling of pollings) {
    let li = document.createElement('li');
    li.textContent = (candidate.party, candidate.district,
                      candidate.state, candidate.policies_supported,
                      candidate.level_government, polling.description,
                      events.description, events.candidates);
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
