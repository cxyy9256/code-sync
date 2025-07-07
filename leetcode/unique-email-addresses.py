class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        
        for email in emails:
            local, domain = email.split("@")
            if '+' in local:x
                local = local[:local.index('+')]
            local = local.replace(".", "")
            email = local + "@" + domain
            unique.add(email)
        return len(unique)