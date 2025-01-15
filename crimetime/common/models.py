import discord

from . import Base

class User(Base):
    '''Stored User Info'''
    balance:  int = 0    #Cash Balance
    p_wins:   int = 0    #Player Mugging Wins
    p_losses: int = 0    #Player Mugging Losses
    p_bonus:  float = 0  #Player Bonus from Win/Loss Ratio
    pve_win: int = 0     #Basic "Mug" win count.
    pve_loss: int = 0    #Basic "Mug" loss count.
    r_wins:   int = 0    #Player Robbery Wins - Upcoming
    r_losses: int = 0    #Player Robbery Losses - Upcoming
    h_wins:   int = 0    #Player Heist Wins - Upcoming
    h_losses: int = 0    #Player Heist Losses - Upcoming
    pop_up_wins: int = 0 #Player Pop-up Challenge victories - upcoming.
    pop_up_loss: int = 0 #Player Pop-up Challenge losses - upcoming.

    # Ratio property sets
    @property # Ratio for player pvp mugging stats
    def p_ratio(self) -> float:
        return (self.p_wins / self.p_losses) if self.p_losses > 0 else self.p_wins
    @property
    def p_ratio_str(self) -> str:
        return f"{self.p_wins}:{self.p_losses}"
    @property  # Ratio for random pop-up mugging challenges
    def pop_up_ratio(self) -> float:
        return (self.pop_up_wins / self.pop_up_loss) if self.pop_up_loss > 0 else self.pop_up_wins    
    @property
    def pop_up_ratio_str(self) -> str:
        return f"{self.pop_up_wins}:{self.pop_up_loss}"

class GuildSettings(Base):
    users: dict[int, User] = {}

    def get_user(self, user: discord.User | int) -> User:
        uid = user if isinstance(user, int) else user.id
        return self.users.setdefault(uid, User())

class DB(Base):
    configs: dict[int, GuildSettings] = {}

    def get_conf(self, guild: discord.Guild | int) -> GuildSettings:
        gid = guild if isinstance(guild, int) else guild.id
        return self.configs.setdefault(gid, GuildSettings())