const text = "     Kung Fu Panda is a beloved animated movie about a clumsy, food-loving panda named Po who dreams of becoming a kung fu master.\nPo's dream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release.\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship.\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages.   ";


function paragraphsArray(str) {
    return str.split('\n');
  }

function replaceFirstMovieWithFilm(str) {
    return str.replace('movie', 'film');
  }

function replacePandaWithBear(str) {
    return str.replaceAll(/Panda/g, 'Bear');
  }

function convertToUppercase(str) {
    return str.toUpperCase();
  }

function convertToLowercase(str) {
    return str.toLowerCase();
  }
function findIndexOfPo(str) {
    return str.indexOf('Po');
  }

function sliceFromPoToEnd(str) {
    const startIndex = str.indexOf('Po');
    return str.slice(startIndex);
  }

function extractWords(str) {
    return str.split(/\s+/).filter((word) => word.length > 0);
  }
function endsWithAges(str) {
    return str.endsWith("ages.");
  }

function addFavoriteMovieText(str) {
    return str + " is one of my favorite movies!";
  }
  
  
