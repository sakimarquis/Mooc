// Exercise 1. Social group reasoning
// a
var sampleGroupPrototype = mem(function(groupName) {
    var prior = repeat(3, function(){return beta({a: 1, b: 1})})
    return _.zipObject(properties, prior)
})
  
var results = Infer({method: 'MCMC', kernel: {HMC: {steps: 10, stepSize: .01}}, 
                    samples: 3000}, function(){
    mapData({data: data}, function(datum) {
        var group = flip() ? "group1" : "group2"
        var prototype = sampleGroupPrototype(group)
        mapData({data: properties}, function(property){
        observe(Bernoulli({p: prototype[property]}), datum[property])
        })
    })
    return {group1: sampleGroupPrototype('group1'), 
            group2: sampleGroupPrototype('group2')}
})

// Exercise 2: Detecting cheating
// b
var results = Infer(inferOpts, function() {
    var group = mem(function(name){
      return flip() ? "bonafide" : "malinger"
    })
    var bonafide = uniform(0.2, 1)
    var malinger = uniform(0, 0.8)
    var accuracy = function(name){
      return group(name) == "bonafide" ? bonafide : malinger
    }
    var obsFn = function(datum){
      observe(Binomial({p: accuracy(datum["subjID"]), n: 45}), datum["score"])
    }
    mapData({data: data}, obsFn)
  
    var subjects = map(function(datum) {
      return group(datum["subjID"])}, data)
    
    return subjects
})