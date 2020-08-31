let deck = [{1: "heart"}, {2: "heart"}, {3: "heart"}, {4: "heart"}, {5: "heart"}, {6: "heart"}, {7: "heart"}, {8: "heart"}, {9: "heart"}, {10: "heart"}, {11: "heart"}, {12: "heart"}, {13: "heart"}, {1: "club"}, {2: "club"}, {3: "club"}, {4: "club"}, {5: "club"}, {6: "club"}, {7: "club"}, {8: "club"}, {9: "club"}, {10: "club"}, {11: "club"}, {12: "club"}, {13: "club"}]
shuffled_deck = shuffle(deck)
hand1 = deal(shuffled_deck)
hand2 = deal(shuffled_deck)
player1_win = war(hand1, hand2)
player2_win = war(hand1, hand2)

function shuffle(deck){
  let shuffled_deck = [];
    // for (i = 0; i < deck.length; i++) {
    let random_position = Math.floor(Math.random() * deck.length);
    shuffled_deck.push(deck.splice(random_position, 1));
  // }
  return shuffled_deck;
}

shuffle(deck)
// console.log(shuffled_deck);

function deal(shuffled_deck){
  let hand1 = [];
  let hand2 = [];
    hand1.push(shuffled_deck.splice(0, 6, 7));
    hand1.push(shuffled_deck.splice(7, 13, 7));
  return hand1;
  return hand2;
}
deal(shuffled_deck)
// console.log(hand1);
// console.log(hand2);

function war(hand1, hand2){
  let player1_card = hand1.pop();
  let player2_card = hand2.pop();
  let player1_win = [];
  let player2_win = [];
  if (player1_card > player2_card){
    player1_win.push(player1_card.pop() && player2_card.pop());
    return player1_win;
  } else if (player1_card < player2_card) {
    player2_win.push(player1_card.pop() && player2_card.pop());
    return player2_win;
  }
}
war(hand1, hand2)

console.log(player1_win)
console.log(player2_win);




//
// deal(shuffled_deck)
// console.log(hand1);
//
// function deal2(shuffled_deck){
// let hand2 = shuffled_deck.splice(7, 13, 7);
// return hand2
// }


// deck = [ 1, 2,  4, 5, 6, 7, 9, 10, J, Q, K, A ]
// shuffled_deck = shuffle(deck)
// function shuffle(deck){
// 	Loop:
// 	decklength = deck.length
// 	position = random number between 1 - and decklength (2)
// 	take from deck at position
// 	and push into shuffled_deck
// 	returns shuffle_deck
// }


//hand.push(deck.splice(Math.floor(Math.random() * deck.length), 1)[0]);

// let position = Math.floor((Math.random() * decklength));
// let take = deck.splice(position, 1);
