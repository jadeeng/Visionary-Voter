function fetchNames(zipcode) {
  fetch(`http://localhost:8080/candidates?q=${zipcode}`)
    .then((resp) => resp.json())
    .then(addNames);
}

function addNames(names) {
  const ul = document.getElementById('Candidates');
  while (ul.firstChild) {
      ul.removeChild(ul.firstChild);
  }
  for (let name of names) {
    const li = document.createElement('li');
    li.textContent = name;
    ul.appendChild(li);
  }
}

function setListener() {
  const inputEl = document.getElementById('dropdown-input');
  inputEl.addEventListener('input', () => {
    fetchNames(inputEl.value);
  });
}

window.onload = setListener;


// var getZipCode = function (country, zip, callback) {
//     var keys = {
//
//             US: 2,
//
//         },
//         patterns = {
//
//             US: /^\d{5}(-\d{4})?$/,
//         },
//         headers = [
//             'countryCode',
//             'postalCode',
//             'placeName',
//             'adminName1',
//             'adminCode1',
//             'adminName2',
//             'adminCode2',
//             'adminName3',
//             'adminCode3',
//             'latitude',
//             'longitude',
//             'accuracy'
//         ],
//         pattern = null,
//         country = country && country.toLocaleUpperCase();
//
//     // Check patterns.
//     if (typeof patterns[country] !== 'undefined') {
//         pattern = patterns[country];
//     }
//     else {
//         for (var k in patterns) {
//             if (patterns.hasOwnProperty(k) && k.indexOf(country) > 0) {
//                 pattern = patterns[k];
//                 break;
//             }
//         }
//     }
//     var result = {
//         input: {
//             country: country,
//             zip: zip
//         },
//         lookup: {},
//         pattern: pattern,
//         validPattern: pattern && pattern.test(zip),
//         validLookup: false,
//         valid: false
//     };
//
//     // Process lookup if pattern is unmatched or validated.
//     if (!result.pattern || result.validPattern) {
//         if (typeof keys[country] !== 'undefined') {
//             // Remove specificity that is beyond our database.
//             if (country === 'US' && zip.indexOf('-') === 5) {
//                 zip = zip.substring(0, zip.indexOf('-'));
//             }
//             window.zipCodesCallback = function (zipCodes) {
//                 if (typeof zipCodes[zip] !== 'undefined') {
//                     for (var i = 0, len = headers.length; i < len; i++) {
//                         result.lookup[headers[i]] = zipCodes[zip][i];
//                     }
//                     result.validLookup = true;
//                     result.valid = true;
//                 }
//                 callback(result);
//             };
//             var k = keys[country] > 0 ? zip.toUpperCase().replace(/[^0-9A-Z]/g, '').substr(0, keys[country]) : 0,
//                 script = document.createElement('script');
//             script.src = 'https://' + country + '.zipcodes.gdn/min/' + k + '.jsonp';
//             document.body.appendChild(script);
//         }
//         else {
//             // Unable to lookup and/or pattern match.
//             result.valid = true;
//             callback(result);
//         }
//     }
// };
//
// getZipCode('US', '90210', function (result) {
//         console.log(result);
//     });'''
