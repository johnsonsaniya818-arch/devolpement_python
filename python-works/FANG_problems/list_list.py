class MergedIntervels:

    def solution(self,intervels):

        merged=[]#[1,3]

        merged.append(intervels[0])#[1,3]

        for lst in intervels:

            if merged[-1][1]>=lst[0]:#3>2#lst[2,5]

                merged[-1][1]=lst[1]#3==5

            else:

                merged.append(lst)

        return merged

merge_instance=MergedIntervels()

print(merge_instance.solution([[1,3],[2,5],[10,15]]))