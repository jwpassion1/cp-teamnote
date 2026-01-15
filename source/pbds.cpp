#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

//중복 비허용 int형 pbds
#define ordered_set tree<int, null_type, less<>, rb_tree_tag, tree_order_statistics_node_update>
//중복 허용 int형 pbds
#define ordered_set tree<int, null_type, less_equal<>, rb_tree_tag, tree_order_statistics_node_update>


ordered_set OS; //pbds OS 선언
OS.insert(val); // OS에 val 삽입
OS.erase(val); // OS에서 val 삭제 (중복 비허용일때)
OS.order_of_key(val); // OS에서 val보다 작은 원소의 개수 리턴
OS.find_by_order(K); // OS[K] 리턴 (0-based-index)

void erase(ordered_set &OS, int val){ // OS에서 val 삭제 (중복 허용일때)
    auto it = OS.find_by_order(OS.order_of_key(val));
    if (*it == val) OS.erase(it);
}