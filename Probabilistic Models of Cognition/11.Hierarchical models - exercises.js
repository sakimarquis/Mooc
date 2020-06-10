// Exercise 2: Rotten apples
// a
var makeBarrel = mem(function(barrel){
  var prior = beta({a: .1, b: .2})
  return function(N){
    return repeat(N, function(){flip(prior)})
  }
})

var abarrel = makeBarrel('b')
abarrel(5)

// b
var makeStore = mem(function(store){
    var para = function(){
        return sample(Categorical({ps: ones([5,1]), vs: [0.1, 0.3, 0.5, 0.7, 0.9]}))
    }
    var prior = beta({a: para(), b: para()})
    return mem(function(barrel){
      return function(N){
        return repeat(N, function(){flip(prior)})
    }})
})


// c
var makeCity = mem(function(city){
    var city_prior = flip()
    var para = city_prior ? function(){
        return sample(Categorical({ps: ones([4,1]), vs: [0.1, 0.2, 0.4, 0.5]}))
    } : function(){
        return sample(Categorical({ps: ones([4,1]), vs: [0.5, 0.6, 0.7, 0.8]}))
    }
    var prior = beta({a: para(), b: para()})
    return mem(function(store){
      return mem(function(barrel){
        return function(N){
          return repeat(N, function(){flip(prior)})
    }})})
    })
// d
var C1 = makeCity("C1")
var S1 = C1("S1")
var B1 = S1("B1")
var S2 = C1("S2")
var B2 = S2("B2")

viz(Infer({method: 'enumerate'}, function(){
  condition(Math.sum(B1(10)) == 7)
  return Math.sum(B2(10))
}))


// Exercise 3: Hierarchical models for BDA
// a
var post = Infer({method: "MCMC",  kernel: {HMC: {steps: 10, stepSize: 1}}, samples: 1000}, function(){
    var groupMeans = {vowel: gaussian(200, 100), consonant: gaussian(200, 100)}
    var wordMeans = mem(function(group, word){
      return group == "vowel" ? gaussian(groupMeans['vowel'], 2) : gaussian(groupMeans['consonant'], 2) 
      // this specific value of sigma = 2 makes the effect dispear
    })
    
    var obsFn = function(d){
      //assume response times (rt) depend on group means with a small fixed noise:
      observe(Gaussian({mu: wordMeans(d.group, d.word),
        sigma: 10}), d.rt)
    }
    
    mapData({data: data}, obsFn)
    
    //explore the difference in means:
    return groupMeans['vowel']-groupMeans['consonant']
})

// b
var post = Infer({method: "MCMC",  kernel: {HMC: {steps: 10, stepSize: 1}}, samples: 1000}, function(){
    var groupMeans = {vowel: gaussian(200, 100), consonant: gaussian(200, 100)}
    var wordMeans = mem(function(group, word){
      return group == "vowel" ? gaussian(groupMeans['vowel'], 2) : gaussian(groupMeans['consonant'], 2) 
      // this specific value of sigma = 2 makes the effect dispear
    })
    var idMeans = mem(function(id, group, word){
        return gaussian(wordMeans(group, word), 1)
    })
    
    var obsFn = function(d){
      //assume response times (rt) depend on group means with a small fixed noise:
      observe(Gaussian({mu: idMeans(d.id, d.group, d.word),
        sigma: 10}), d.rt)
    }
    
    mapData({data: data}, obsFn)
    
    //explore the difference in means:
    return groupMeans['vowel']-groupMeans['consonant']
})

