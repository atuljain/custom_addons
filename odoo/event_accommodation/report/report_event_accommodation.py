# -*- coding: utf-8 -*-

from openerp import models, fields
from openerp import tools


class report_event_registration(models.Model):
    """Event Accomodations Analysis"""
    _name = "report.event.accommodation"
    _auto = False

    accommodation_id = fields.Many2one('event.accommodation', 'Accommodations', required=True)
    draft_state = fields.Integer(' # No of Draft Accommodations')
    confirm_state = fields.Integer(' # No of Confirmed Accommodations')
    nbaccommodation = fields.Integer('Number of Accommodation')
    accommodation_state = fields.Selection([('available', 'Available'), ('booked', 'Booked')], 'Accommodation State', readonly=True, required=True)
    event_id = fields.Many2one('event.event', 'Event', required=True)
    partner_id = fields.Many2one('res.partner', 'Owner', readonly=True)

    def init(self, cr):
        """Initialize the sql view for the event registration """
        tools.drop_view_if_exists(cr, 'report_event_accommodation')

        # TOFIX this request won't select events that have no registration
        cr.execute(""" CREATE VIEW report_event_accommodation AS (
            SELECT
                a.id::varchar AS id,
                a.id AS accommodation_id,
                a.partner_id AS partner_id,
                r.event_id AS event_id,
                count(a.id) AS nbaccommodation,
                CASE WHEN a.state IN ('available') THEN r.nb_register ELSE 0 END AS draft_state,
                CASE WHEN a.state IN ('booked') THEN r.nb_register ELSE 0 END AS confirm_state,
                a.state AS accommodation_state,
                r.state AS registration_state
            FROM
                event_accommodation a
                LEFT JOIN event_registration r ON (a.id=r.event_id)

            GROUP BY
                accommodation_id,
                r.id,
                event_id,
                accommodation_state,
                r.nb_register,
                a.id,
                a.partner_id,
                accommodation_state
        )
        """)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
