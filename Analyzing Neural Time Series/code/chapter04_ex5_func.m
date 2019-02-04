function y = chapter04_ex5_func(rows,columns)

mat = rand(rows,columns);
y = mat < 0.5;

for i = 1:size(mat,1)
    for j = 1:size(mat,2)
        if mat(i,j) < 0.5
            switch i
                case 1
                    row_excep = 'st';
                case 2
                    row_excep = 'nd';
                case 3
                    row_excep = 'rd';
                otherwise
                    row_excep = 'th';
            end
            switch j
                case 1
                    column_excep = 'st';
                case 2
                    column_excep = 'nd';
                case 3
                    column_excep = 'rd';
                otherwise
                    column_excep = 'th';
            end
            disp(['The ' num2str(i) row_excep ' row and ' num2str(j) column_excep ' column has a value of ' num2str(mat(i,j)) ' and is not bigger than 0.5.'])
        end
    end
end
end