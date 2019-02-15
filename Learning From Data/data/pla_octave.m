%
%The octave code shows the behavior of the perceptron learning algorithm when using data *without* x_0 [or with x_0 = 0]
%The algorithm finds the first (in a cyclic sense) misclassified point and update the weights based on the point.
%The dark blue line is the boundary defined by the current weights, which are depicted by the black line pointing to the magenta square.
%The light blue point is the point being explored (correct or wrong).
%When the point is wrongly classified, the red line indicates the change to the weights, and the purple line indicates the new weights.
%author: Hsuan-Tien Lin for the book "Learning From Data" (http://amlbook.com)
%released under GPL 3.0
%THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
%``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
%LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
%A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR
%CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
%EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
%PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
%PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
%LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
%NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
%SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

X = rand(20, 2);
Y = (X(:, 1) > X(:, 2)) * 2 - 1;
T = 1000;
N = size(X, 1);
D = size(X, 2);

XX = [zeros(N, 1), X];

ww = zeros(3, 1);

stoptoken = 0;

ispos = (Y > 0);
pos = find(ispos);
neg = find(~ispos);

minX1 = 0; %min(X(:, 1));
maxX1 = 1; %max(X(:, 1));
minX2 = 0; %min(X(:, 2));
maxX2 = 1; %max(X(:, 2));

gridX1 = (maxX1 - minX1) ./ 100;
gridX2 = (maxX2 - minX2) ./ 100;

minX1 = minX1 - 100 * gridX1;
maxX1 = maxX1 + 100 * gridX1;
minX2 = minX2 - 100 * gridX2;
maxX2 = maxX2 + 100 * gridX2;

[bigX1, bigX2] = meshgrid(minX1:gridX1:maxX1, minX2:gridX2:maxX2);
nTest=size(bigX1, 1) * size(bigX1, 2);
TX = [reshape(bigX1, nTest, 1), reshape(bigX2, nTest, 1)];

iter = 0;
for t=1:T
%% Draw   
  clf;
  axis([minX1 maxX1 minX2 maxX2]);
  axis square;
  hold on;
  
  if ww(2) ~= 0
    minA = - (ww(3) * minX2 + ww(1)) ./ ww(2);
    maxA = - (ww(3) * maxX2 + ww(1)) ./ ww(2);
    H = line([minA, maxA], [minX2, maxX2]);
    hold on;
    set(H, 'LineStyle', '-.', 'Linewidth', 3, 'Color', [0 0 1])
  end

  if ww(3) ~= 0
    minB = - (ww(2) * minX1 + ww(1)) ./ ww(3);
    maxB = - (ww(2) * maxX1 + ww(1)) ./ ww(3);
    H = line([minX1, maxX1], [minB, maxB]);
    hold on;
    set(H, 'LineStyle', '-.', 'Linewidth', 3, 'Color', [0 0 1])
  end
  

  hold on;
  line([0 ww(2)], [0 ww(3)]);
  hold on;
  plot(ww(2), ww(3), 'md', 'MarkerSize', 20);

  sel = mod(t, N) + 1;
  for n=1:N
    hold on;
    if Y(n) > 0
      symbol = 'o';
    else
      symbol = 'x';
    end
    fontsize = 20;
    if (n ~= sel)
      text(X(n, 1), X(n, 2), symbol, 'FontSize', fontsize);
    else
      text(X(n, 1), X(n, 2), symbol, 'FontSize', fontsize, ...
           'Color', [0 1 1]);
    end    
  end
  
  if (Y(sel) * XX(sel, :) * ww <= 0)
    iter = iter + 1; %count one iteration
    ww = ww + Y(sel) * XX(sel, :)';
    hold on;
    if Y(sel) > 0
      symbol = 'o';
    else
      symbol = 'x';
    end
    text(X(sel, 1), X(sel, 2), symbol, 'FontSize', fontsize, ...
         'Color', [1 0 0]);
    hold on;
    line([0, X(sel, 1)], [0, X(sel, 2)], 'Color', [0 1 0]);
    line([0, Y(sel) * X(sel, 1)], [0, Y(sel) * X(sel, 2)], 'Color', [1 0 0]);
    hold on;
    line([0 ww(2)], [0 ww(3)], 'Color', [1 0 1]);
  end
  
  drawnow;  
  pause(0.5);
  hold off;
end

w = ww(2:3);
b = ww(1);


