Fe = 100; # Hz
duree = 10 ; # secondes
t = [1/Fe:1/Fe:duree];
f0 = 20; # Hz
m = cos(2*pi*f0*t);
T = 0.25; # secondes
D = 2; # secondes
x(1:length(t)) = 0;

for i = 0:duree/D-T
  x(i*Fe*D+1:i*Fe*D+T*Fe) = 1;
end

s = m.*x;

figure;
subplot(311);plot(t,m) ; ylabel('figure 1a');
subplot(312);plot(t,x) ; ylabel('figure 1b');
subplot(313);plot(t,s) ; ylabel('figure 1c');

M = 4096;
S = fft(s, M);
f = [0:M-1]/M*Fe;

figure;subplot(211); plot(f, abs(S)) ; ylabel('figure 2a');

figure; plot(t, s); ylabel('Q8');