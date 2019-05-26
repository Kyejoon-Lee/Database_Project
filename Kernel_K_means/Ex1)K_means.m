load X.mat

x = X(1:end,1:end); 

init = [1,2,3,4,5];
k =5;
c = K(k,init,x);

function [cluster] = K(k,init_center,x)
    x1_train = x(1:end,1);
    x2_train = x(1:end,2);
    flag = 0;
    objl = [];
    for i=1:k
        centroid(i,1) = x1_train(init_center(i));
        centroid(i,2) = x2_train(init_center(i));
    end
    iteration = 1;
    while 1
        
        if flag == 1
            tcluster = cluster;
            tempobj = obj;
        end
        
        cluster = [];
        obj = 0;
        for i=1:1000
            temp = 10000;
            cur = 0;
            mini = [];
            for j=1:k
                cnt = sqrt((x1_train(i)- centroid(j,1))^2 + (x2_train(i) -centroid(j,2))^2);
                mini(end+1) = cnt;
            end
            for w=1:k
                if mini(w) == min(mini)
                    if flag == 0
                    obj = obj + mini(w);
                    end
                    cur = w;
                    cflag = 0;
                    if flag == 1
                        for p =1:1000
                            if tcluster(cur,p) == i
                                cflag =1;
                            end
                        end
                    end
                    if cflag == 1
                        continue
                    end
                    if cflag == 0
                        obj = obj + mini(w);
                    end
                end
            end
            cluster(cur,end+1) = i;
        end
        if flag == 0 
            objl(iteration) = obj;
        end
        if flag ==1
            objl(iteration) = obj;
            if obj == tempobj  
                figure(1);
                plot(1:iteration,objl,'o-');
                xlabel('iteration');
                ylabel('objective Value');
                figure(2);
                for i = 1:k
                    for j = 1:1000
                        if cluster(i,j) > 0
                            if i == 1
                                plot(x(cluster(i,j),1),x(cluster(i,j),2),'*b');
                                hold on
                            end
                            if i ==2
                                plot(x(cluster(i,j),1),x(cluster(i,j),2),'*m');
                            end
                            if i ==3
                                plot(x(cluster(i,j),1),x(cluster(i,j),2),'*g');
                            end
                            if i == 4
                            plot(x(cluster(i,j),1),x(cluster(i,j),2),'*k');
                            end
                            if i ==5
                               plot(x(cluster(i,j),1),x(cluster(i,j),2),'*r');
                            end
                        end
                    end
                end
                plot(centroid(:,1),centroid(:,2),'o');
                hold off
                break    
            end
        end
        for j=1:k
            temp1 = 0;
            temp2 = 0;
            num =0;
                for i=1:1000
                    if cluster(j,i) > 0
                        temp1 = x(cluster(j,i),1)+temp1;
                        temp2 = x(cluster(j,i),2)+temp2;
                        num = num+1;
                    end
                end
            centroid(j,1) = temp1/num;
            centroid(j,2) = temp2/num;
        end
        flag = 1;
        iteration = iteration+1;
    end
end

