// Exercise 1: Fair coins and biased coins

// a)
var model = function() {
    return flip() ? 'H' : 'T'
  }
  var log_prob = Infer({method:'enumerate'}, model).score('H')
Math.exp(log_prob)



// bcd)
var model = function(){
    var whichcoin = mem(function(){
        return flip()
    })
    var coin = function(){
        return whichcoin() ? flip(0.9) : flip()
    }
    var A = coin()
    var B = coin()
    var C = coin()
    condition(A + B == 2)
    return C
}
viz(Infer({method:'enumerate'}, model))


// Exercise 2: Conditioning and Intervention
// a)  same, because in this, lung cancer and cold are *correlate* with cough. 
var model = function(){
    var lungCancer = 1; // flip(0.01)
    var cold = flip(0.2);
    var cough = (
      (cold && flip(0.5)) || (lungCancer && flip(0.3))
    )
    // condition(lungCancer == 1) 
    return cough
  }
Infer({method:'enumerate'}, model)

// b)  we want to make it 'causal'(a priori)
// intervening
var model = function(){
  var cold = flip(0.2);
  var lungCancer = 1;
  var cough = (
    (cold * flip(0.5)) || (lungCancer * flip(0.3))
  )
  //condition(lungCancer == 1)
  return cough
}
Infer({method:'enumerate'}, model)

// conditioning, in this scenario, all people must have cold
var model = function(){
  var cold = flip(0.2);
  var lungCancer = flip(0.01) * cold;
  var cough = (
    (cold * flip(0.5)) || (lungCancer * flip(0.3))
  )
  condition(lungCancer == 1)
  return cough
}
Infer({method:'enumerate'}, model)


// Exercise 4: Extending the smiles model
// b)
var extendedSmilesModel = function() {
  var nice = mem(function(person) {return flip(.7)});
  var want = function(person) {return nice(person) ? flip(.3) : flip(.7);}
  var smiles = function(person) {
    return nice(person) ? flip(.8) : flip(.5) || want(person) ? flip(.7) : flip(.3);
  }
  return smiles('alice')
}

Infer({method: "enumerate"}, extendedSmilesModel)

// c)

var extendedSmilesModel = function() {
  var nice = mem(function(person) {return flip(.7)});
  var want = function(person) {return nice(person) ? flip(.3) : flip(.7);}
  var smiles = function(person) {
    return nice(person) ? flip(.8) : flip(.5) || want(person) ? flip(.7) : flip(.3);
  }
  condition(!smiles('bob') && !smiles('bob') && !smiles('bob'));
  return want('bob')
}

Infer({method: "enumerate"}, extendedSmilesModel)


// Exercise 5: Sprinklers, Rain and mem
// a) : (0.5*(1-0.3) + 0.5*0.3) / (0.5*(1-0.3) + 0.5*0.3 + 0.3*(1-0.5))
var wetGarden = function() {
  var sprinkled = flip();
  var rained = flip(0.3);
  var wet = sprinkled || rained;
  condition(wet == 1);
  return sprinkled
}
Infer({method: "enumerate"}, wetGarden)

// b) : 
var wetGarden = function() {
  var sprinkled1 = flip();
  var sprinkled2 = flip();
  var rained = flip(0.3);
  var wet1 = sprinkled1 || rained;
  var wet2 = sprinkled2 || rained;
  condition(wet1 == 1 && wet2 == 1);
  return rained
}
Infer({method: "enumerate"}, wetGarden)

// c) : 
var wetGarden = function() {
  var sprinkled = mem(function(person) {return flip()});
  var rained = flip(0.3);
  var wet = function(person) {
    return sprinkled(person) || rained
  };
  condition(wet('me') == 1 && wet('Kevin') == 1 && wet('Manu') == 1 && wet('Josh') == 1 && wet('Kelsey') == 1);
  return rained
}
Infer({method: "enumerate"}, wetGarden)

// Exercise 6: Casino game 
// c)

// define some variables and utility functions
var checkVowel = function(letter) {return _.includes(['a', 'e', 'i', 'o', 'u'], letter);}
var letterVals = ['g', 'a', 'm', 'e'];
var letterProbs = map(function(letter) {return checkVowel(letter) ? 0.45 : 0.05;}, letterVals);
var letters = Categorical({vs: letterVals, ps: letterProbs})

// Compute p(h | win)
var distribution = Infer({method: 'enumerate'}, function() {
  var letter = sample(letters);
  var position = letterVals.indexOf(letter) + 1; 
  var winProb = 1 / Math.pow(position, 2);
  condition(flip(winProb) == 1)
  return letter
});

viz.auto(distribution);

// d)
//condition(flip(winProb) == 1)
//return checkVowel(letter)