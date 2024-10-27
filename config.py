"""项目配置"""

# 图灵机器人，99元一月付费版，尽情享用！
tuling_api_key = '88f17f853d974387af64955bed9466f4'

# 自动回复
is_friend_auto_reply = False  # 好友自动回复
is_group_reply = False  # 此项表示群中是否回复
is_group_at_reply = False  # 上一项开启后此项才生效
is_forward_revoke_msg = False  # 开启防撤回模式
is_forward_group_at_msg = False  # 转发群@我的消息
# 控制是否转发主人群的消息
is_forward_master_group_msg = True


# 机器人主人
bot_master_name = '天然有机 笑笑'  # 使用备注名更安全，只允许一个，可远程控制机器人，如果不设置(空)则将文件助手设置为管理员，但不具备远程控制功能

# 监听某些好友群聊，如老板
is_listen_friend = False
listen_friend_names = ''  # 需要监听的人名称，使用备注名更安全，允许多个用|分隔，如：主管|项目经理|产品狗
listen_friend_groups = ''  # 在这些群里监听好友说的话，匹配模式：包含“唯一集团工作群”的群


# 转发信息至群
is_forward_mode = True  # 打开转发模式，主人发送给机器人的消息都将转发至forward_groups群
forward_groups = ['智能小助手',''] #'Python新手交流'  # 需要将消息转发的群，匹配模式同上

# 群分享监控
is_listen_sharing = False
listen_sharing_groups = '智能小助手'  # 监控群分享，匹配模式同上


# 新增变量: 机器人主人群
# 修改时间: 2023年4月15日
# 修改原因: 为了支持将整个群组设置为机器人的主人,增加管理灵活性
# 修改人: sunnyzhang
master_group_name = "智能小助手"  # 机器人主人群的ID,请将"群ID"替换为实际的群组ID

# 如果需要支持多个主人群,可以使用以下格式:
# master_group_name = ["群ID1", "群ID2", "群ID3"]  # 机器人主人群的ID列表
# 定义主人群和对应的转发群清单，其中键表示主人群，值是一个列表，包含需要将主人群消息转发到的其他群。
master_group_forward_map = {
    "智能小助手": ["禾风 天然有机","多多严选"]
 #   "测试群3": ["测试群4", "测试群5","测试群1"]
}


