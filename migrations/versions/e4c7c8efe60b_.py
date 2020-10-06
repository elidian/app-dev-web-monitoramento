"""empty message

Revision ID: e4c7c8efe60b
Revises: 
Create Date: 2020-10-05 21:06:04.779968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4c7c8efe60b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cam',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('account_type', sa.String(length=15), nullable=True),
    sa.Column('end', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cam_end'), 'cam', ['end'], unique=False)
    op.create_index(op.f('ix_cam_name'), 'cam', ['name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('account_type', sa.String(length=15), nullable=True),
    sa.Column('cpf', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_cpf'), 'user', ['cpf'], unique=True)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('placa', sa.String(length=7), nullable=True),
    sa.Column('chassi', sa.String(length=17), nullable=True),
    sa.Column('cpf_dono', sa.String(length=11), nullable=True),
    sa.Column('queixa_roubo', sa.Boolean(), nullable=True),
    sa.Column('licenciamento', sa.Boolean(), nullable=True),
    sa.Column('exercicio', sa.String(), nullable=True),
    sa.Column('ipva', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vehicle_chassi'), 'vehicle', ['chassi'], unique=True)
    op.create_index(op.f('ix_vehicle_cpf_dono'), 'vehicle', ['cpf_dono'], unique=False)
    op.create_index(op.f('ix_vehicle_placa'), 'vehicle', ['placa'], unique=True)
    op.create_index(op.f('ix_vehicle_queixa_roubo'), 'vehicle', ['queixa_roubo'], unique=False)
    op.create_table('postcam',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('info', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('cam_id', sa.Integer(), nullable=True),
    sa.Column('cam_name', sa.String(length=64), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_placa', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['cam_id'], ['cam.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_postcam_cam_id'), 'postcam', ['cam_id'], unique=False)
    op.create_index(op.f('ix_postcam_cam_name'), 'postcam', ['cam_name'], unique=False)
    op.create_index(op.f('ix_postcam_timestamp'), 'postcam', ['timestamp'], unique=False)
    op.create_index(op.f('ix_postcam_vehicle_id'), 'postcam', ['vehicle_id'], unique=False)
    op.create_index(op.f('ix_postcam_vehicle_placa'), 'postcam', ['vehicle_placa'], unique=False)
    op.create_table('postuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('info', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_name', sa.String(length=64), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_placa', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_postuser_timestamp'), 'postuser', ['timestamp'], unique=False)
    op.create_index(op.f('ix_postuser_user_id'), 'postuser', ['user_id'], unique=False)
    op.create_index(op.f('ix_postuser_user_name'), 'postuser', ['user_name'], unique=False)
    op.create_index(op.f('ix_postuser_vehicle_id'), 'postuser', ['vehicle_id'], unique=False)
    op.create_index(op.f('ix_postuser_vehicle_placa'), 'postuser', ['vehicle_placa'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_postuser_vehicle_placa'), table_name='postuser')
    op.drop_index(op.f('ix_postuser_vehicle_id'), table_name='postuser')
    op.drop_index(op.f('ix_postuser_user_name'), table_name='postuser')
    op.drop_index(op.f('ix_postuser_user_id'), table_name='postuser')
    op.drop_index(op.f('ix_postuser_timestamp'), table_name='postuser')
    op.drop_table('postuser')
    op.drop_index(op.f('ix_postcam_vehicle_placa'), table_name='postcam')
    op.drop_index(op.f('ix_postcam_vehicle_id'), table_name='postcam')
    op.drop_index(op.f('ix_postcam_timestamp'), table_name='postcam')
    op.drop_index(op.f('ix_postcam_cam_name'), table_name='postcam')
    op.drop_index(op.f('ix_postcam_cam_id'), table_name='postcam')
    op.drop_table('postcam')
    op.drop_index(op.f('ix_vehicle_queixa_roubo'), table_name='vehicle')
    op.drop_index(op.f('ix_vehicle_placa'), table_name='vehicle')
    op.drop_index(op.f('ix_vehicle_cpf_dono'), table_name='vehicle')
    op.drop_index(op.f('ix_vehicle_chassi'), table_name='vehicle')
    op.drop_table('vehicle')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_cpf'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_cam_name'), table_name='cam')
    op.drop_index(op.f('ix_cam_end'), table_name='cam')
    op.drop_table('cam')
    # ### end Alembic commands ###
