# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        domains_dict = defaultdict(int)

        for cpdomain in cpdomains:
            count, sub_domain = cpdomain.split()
            domains = sub_domain.split(".")
            domains_dict[".".join(domains)] += int(count)
            domains_dict[".".join(domains[1:])] += int(count)
            if domains[2:]:  # To check conditions for the situations like "wiki.org"
                domains_dict[domains[2]] += int(count)

        for key, value in domains_dict.items():
            ans.append(f"{value} {key}")

        return ans

