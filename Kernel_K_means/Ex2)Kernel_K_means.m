load Y.mat

y = Y(:,:);
init =[1,599];
c =1;
k =2;
res = Kernel(k,init,c,y);
figure(1);
hold on
for i =1:size(res,1)
    for j =1:size(res,2)
        if res(i,j) ~= 0
            if i ==1
                plot(y(res(i,j),1),y(res(i,j),2),'*r');
            end
            if i ==2
                plot(y(res(i,j),1),y(res(i,j),2),'*b');
            end
        end
    end
end
xlabel('x1');
ylabel('x2');
hold off
figure(2);
hold on
for i =1:size(res,1)
    for j =1:size(res,2)
        if res(i,j) ~= 0
            if i ==1
                plot(((y(res(i,j),1)-y(res(i,j),1))^2) - y(res(i,j),1),((y(res(i,j),2)-y(res(i,j),2))^2)-y(res(i,j),2),'*r');
            end
            if i ==2
                plot(((y(res(i,j),1)-y(res(i,j),1))^2) - y(res(i,j),1),((y(res(i,j),2)-y(res(i,j),2))^2)-y(res(i,j),2),'*b');
            end
        end
    end
end
xlabel('x1^2 - x1');
ylabel('x2^2 - x2');
hold off
function [cluster] = Kernel(k,init,c,y)
    y1_train = y(:,1);
    y2_train = y(:,2);
    cluster = [];
    for i=1:k
        cluster(i,:) = init(i);
    end
    while 1
 
        tcluster = cluster;
        for w = 1:600
            mini = [];
            for i=1:k
                temp1 = 0;
                temp2 = 0;
                num =1;
                for j=1:size(cluster,2)
                    if cluster(i,j) ~= 0
                        temp1 = temp1 + exp(-c*((y1_train(cluster(i,j)) - y1_train(w))^2 + (y2_train(cluster(i,j)) - y2_train(w))^2));
                        num = num+1;
                        for n=1:size(cluster(i),2)
                            if cluster(i,n) ~= 0
                                temp2 = temp2 + exp(-c*((y1_train(cluster(i,j)) - y1_train(i,n))^2 + (y2_train(cluster(i,j)) - y2_train(i,n))^2));
                            end
                        end
                    end
                end
                cnt = 1 -2*(temp1/num) + temp2/((num)^2);
                mini(end+1) = cnt;
                
            end
            for i =1:k
                if min(mini)==mini(i)
                    if find(cluster(i)== w)
                        break;
                    else
                        if find(cluster == w)
                            [a,b] = find(cluster ==w);
                            cluster(a,b) = 0;
                            for o=1:size(cluster,2)
                                if cluster(i,o)==0
                                    cluster(i,o) = w;
                                    break;
                                end
                            end
                        else
                            cluster(i,end+1) = w;
                        end
                    end
                end
            end
        end
 
        if size(cluster) == size(tcluster)
            flag1 = 0;
            for i =1:k
                for j =1:size(cluster)
                    if tcluster(i,j) ~= cluster(i,j)
                        flag1 =1;
                        
                        break;
                    end
                end
            end
        
            if flag1 ==0
                break
             end
        end
    end
end