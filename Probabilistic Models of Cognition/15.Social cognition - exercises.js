// Exercise 1: Tricky Agents
// a)
var chooseAction = function(goal, transition, state, deceive) {
    return Infer({method: 'enumerate'}, function() {
      var action = sample(actionPrior);
      condition(deceive ? !goal(transition(state, action)) : goal(transition(state, action)))
      return action;
    })
  };
  
var goalPosterior = Infer({method: 'enumerate'}, function() {
    var deceive = flip();
    var goalFood = sample(foodPrior);
    var goal = function(outcome) {return outcome == goalFood};
    var sallyActionDist = chooseAction(goal, vendingMachine, 'state', deceive);
    condition(deceive == 1 && sample(sallyActionDist) == 'b')
    return goalFood;
});

// b
var goalPosterior = Infer({method: 'enumerate'}, function() {
    var deceive = flip();
    var goalFood = sample(foodPrior);
    var goal = function(outcome) {return outcome == goalFood};
    var sallyActionDist = chooseAction(goal, vendingMachine, 'state', deceive);
    condition(sample(sallyActionDist) == 'b' && sample(sallyActionDist) == 'b')
    return deceive;
});

// Exercise 2: Monty Hall
// Here's a function that might be handy: it removes some set of badItems from a list l
// e.g. removeBadItems(['nut', 'cake', 'nut', 'bagel'], ['cake', 'bagel']) => ['nut', 'nut']
// 这个代码跑不出来，内存占用过大，总是崩溃
var removeBadItems = function(l, badItems) {
    return reduce(function(badItem, remainingL) {
      return remove(badItem, remainingL)
    }, l, badItems);
  }
  
var doors = [1,2,3]

var montyRandom = function(aliceDoor, prizeDoor) {
    return Infer({method: 'enumerate'}, function() {
        return categorical({vs: doors, ps: [1/3, 1/3, 1/3]})
    })
};

var montyAvoidBoth = function(aliceDoor, prizeDoor) {
    return Infer({method: 'enumerate'}, function() {
        var reveal = categorical({vs: doors, ps: [1/3, 1/3, 1/3]})
        condition(reveal != aliceDoor && reveal != prizeDoor)
        return reveal
    })
};

var montyAvoidAlice = function(aliceDoor, prizeDoor) {
    return Infer({method: 'enumerate'}, function() {
        var reveal = categorical({vs: doors, ps: [1/3, 1/3, 1/3]})
        condition(reveal != aliceDoor)
        return reveal
    })
};

var montyAvoidPrize = function(aliceDoor, prizeDoor) {
    return Infer({method: 'enumerate'}, function() {
        var reveal = categorical({vs: doors, ps: [1/3, 1/3, 1/3]})
        condition(reveal != prizeDoor)
        return reveal
    })
};

Infer({method: 'enumerate'}, function() {
    var aliceDoor = categorical({vs: doors, ps: [1/3, 1/3, 1/3]})
    var prizeDoor = categorical({vs: doors, ps: [1/3, 1/3, 1/3]})
    var montyFunction = categorical({vs: [montyRandom, montyAvoidAlice, montyAvoidPrize], ps: [1/3, 1/3, 1/3]})
    var montyDoorDist = montyFunction(aliceDoor, prizeDoor);
    var remaining = removeBadItems(doors, sample(montyDoorDist))
    var choose = categorical({vs: remaining, ps: [1/2, 1/2]})
    factor(montyFunction == montyAvoidBoth)
    return choose == prizeDoor
});