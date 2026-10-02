from homeassistant.util.dt import as_utc, parse_datetime


class OctoplusScratchcardResponse:
  def __init__(self, active_session: dict | None, scratchcard: dict | None):
    self.has_active_session = active_session is not None
    self.has_scratchcard = scratchcard is not None
    session = active_session or {}
    card = scratchcard or {}
    offer = card.get("offer") or {}
    prize = card.get("prize") or {}
    self.starts_at = as_utc(parse_datetime(session["startsAt"])) if session.get("startsAt") is not None else None
    self.ends_at = as_utc(parse_datetime(session["endsAt"])) if session.get("endsAt") is not None else None
    self.session_external_reference = session.get("externalReference")
    self.scratchcard_external_reference = card.get("externalReference")
    self.scratchcard_status = card.get("status")
    self.offer_slug = offer.get("slug")
    self.feature_display_text = offer.get("featureDisplayText")
    self.prize_type = prize.get("__typename")

  def to_dict(self):
    return {
      "starts_at": self.starts_at,
      "ends_at": self.ends_at,
      "session_external_reference": self.session_external_reference,
      "scratchcard_external_reference": self.scratchcard_external_reference,
      "scratchcard_status": self.scratchcard_status,
      "offer_slug": self.offer_slug,
      "feature_display_text": self.feature_display_text,
      "prize_type": self.prize_type,
    }


class RedeemOctoplusPointsResponse:
  is_successful: bool
  errors: list[str]

  def __init__(
    self,
    is_successful: bool,
    errors: list[str]
  ):
    self.is_successful = is_successful
    self.errors = errors