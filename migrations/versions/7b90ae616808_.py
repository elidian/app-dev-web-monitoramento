"""empty message

Revision ID: 7b90ae616808
Revises: ffc759109753
Create Date: 2020-09-14 20:15:54.412551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b90ae616808'
down_revision = 'ffc759109753'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vehicle_queixa_roubo'), table_name='vehicle')
    op.drop_index(op.f('ix_vehicle_placa'), table_name='vehicle')
    op.drop_index(op.f('ix_vehicle_cpf_dono'), table_name='vehicle')
    op.drop_index(op.f('ix_vehicle_chassi'), table_name='vehicle')
    op.drop_table('vehicle')
    # ### end Alembic commands ###