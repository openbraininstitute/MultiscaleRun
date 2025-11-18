### Not an IntEnum because numba may complain
class MIdx:
    # name -> comment
    _names_with_comments = {
        "h_m_n": "1",
        "k_m_n": "2",
        "mg2_m_n": "3",
        "atp_m_n": "8",
        "adp_m_n": "9",
        "notBigg_ATP_mx_m_n": "10",
        "notBigg_ADP_mx_m_n": "11",
        "notBigg_MitoMembrPotent_m_n": "19",
        "h_i_n": "22",
    }

    def __init__(self):
        # Populate progressive indexes dynamically
        self._name_to_index = {}
        for i, name in enumerate(self._names_with_comments.keys()):
            setattr(self, name, i)

    @property
    def size(self):
        return len(self._names_with_comments)

    def get_comment(self, name: str) -> str:
        """Return the original comment for a variable name."""
        return self._names_with_comments.get(name, "")

    def as_dict(self) -> dict:
        """Return a dict of variable names -> progressive indexes."""
        return self._names_with_comments

    def __str__(self) -> str:
        lines = [
            f"{name}: {getattr(self, name)} #{self.get_comment(name)}"
            for name in self._names_with_comments.keys()
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    midx = MIdx()
    print("Indexes:")
    print(midx)
    print(f"Total: {midx.size}")
