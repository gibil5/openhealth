# 13 Sep 2019


This is a very dangerous thing to do. Should NEVER be done:

# Container
#container_id = fields.Many2one(
#	'openhealth.container',
#	ondelete='cascade',		# Very Dangerous. When Container is removed, Patient is removed.
#)
