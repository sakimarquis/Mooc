// Exercise 1. Sampling Implicit Curves
// the markov chains are constrained in local

// b
var onCurve = function(x, y) {
    var x2 = x*x;
    var term1 = y - Math.pow(x2, 1/3);
    var crossSection = x2 + term1*term1 - 1;
    return Math.abs(crossSection) < 0.01;
  };
  var xbounds = [-1, 1];
  var ybounds = [-1, 1.6];
  
  var xmu = 0.5 * (xbounds[0] + xbounds[1]);
  var ymu = 0.5 * (ybounds[0] + ybounds[1]);
  var xsigma = 0.5 * (xbounds[1] - xbounds[0]);
  var ysigma = 0.5 * (ybounds[1] - ybounds[0]);
  var model = function() {
    var b = sample(DiagCovGaussian({mu: Vector([xmu, ymu]), sigma: Vector([xsigma, ysigma])}))
    var x = T.get(b, 0)
    var y = T.get(b, 1)
    condition(onCurve(x, y));
    return {x: x, y: y};
  };
  
  var post = Infer({method: 'MCMC', samples: 5000, lag: 10}, model);
  viz.auto(post);


// Exercise 2. Properties and pitfalls of Metropolis-Hastings
// a : highly positive correlated
viz(marginalize(posterior, function(x) {return x.point2}))
viz(marginalize(posterior, function(x) {return x.interpolationWeight}))
// joint marginal distribution of point2 and interpolationWeigh
viz(marginalize(posterior, function(x) {return {point2: x.point2, interpolationWeigh: x.interpolationWeight}}))


// b
var posterior = Infer({
    method: 'MCMC',
    samples: 100,
    lag: 0,
  }, model)
  
var samples = map(function(d){
    return d["value"]["pointInMiddle"]
}, posterior.samples);
viz.line(_.range(samples.length), samples)

// c: no, the support is really large and prior doesn't have much information

// d: a acceptance rate is around 0.5
